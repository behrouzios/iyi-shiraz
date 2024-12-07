from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import psycopg2
from psycopg2 import sql
import jdatetime
from apps.report_builder.management import database
import json
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from apps.report_builder.management.pagination import CustomPageNumberPagination
import os
from multiprocessing import Pool, cpu_count


class ChartDataView(APIView):
    def post(self, request, *args, **kwargs):
        dbConnectInfo = database.database_connection()
        try:
            connection = psycopg2.connect(dbConnectInfo)
            print("Connection to the database was successful.")
            cursor = connection.cursor()
            data = request.data.get('dcs1h_chart_data')
            if not data:
                return Response({"error": "No data provided"}, status=status.HTTP_400_BAD_REQUEST)
            table = data.get('table')
            order_by = data.get('order_by')
            query = sql.SQL("SELECT * FROM {table} ORDER BY {order_by} DESC LIMIT 50").format(
                table=sql.Identifier(table),
                order_by=sql.Identifier(order_by)
            )
            print(f"Executing query: {query.as_string(connection)}")
            cursor.execute(query)
            results = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            cursor.close()
            connection.close()
            print("Connection closed.")
            results_dict = [dict(zip(columns, row)) for row in results]
            print(f"Results: {results_dict}")
            return Response(results_dict, status=status.HTTP_200_OK)

        except Exception as error:
            print(f"Error: {error}")
            return Response({"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from urllib.parse import urlparse, urlencode, parse_qsl, urlunparse
from psycopg2 import sql

from multiprocessing import Pool, cpu_count

# Define the helper function at the global level
def row_to_dict(row, columns):
    return dict(zip(columns, row))

class Dcs1hChartDataViewFilter(APIView):
    pagination_class = CustomPageNumberPagination

    def get(self, request, *args, **kwargs):
        dbConnectInfo = database.database_connection()
        try:
            connection = psycopg2.connect(dbConnectInfo)
            print("Connection to the database was successful.")
            cursor = connection.cursor()

            # Extract 'start_date' and 'end_date' from query parameters
            start_date_jalali = request.query_params.get('start_date')
            end_date_jalali = request.query_params.get('end_date')

            if not start_date_jalali or not end_date_jalali:
                return Response({"error": "Both start_date and end_date are required"}, status=status.HTTP_400_BAD_REQUEST)

            # Convert the dates to integer format
            start_date_int = int(start_date_jalali.replace('-', ''))
            end_date_int = int(end_date_jalali.replace('-', ''))

            # Get table name from query parameters (default to 'dcs1h')
            table = request.query_params.get('table', 'dcs1h')

            # Build the query to fetch data
            query = sql.SQL("""
                SELECT * FROM {table}
                WHERE date BETWEEN %s AND %s
                ORDER BY date DESC
            """).format(table=sql.Identifier(table))

            print(f"Executing query: {query.as_string(connection)} with params ({start_date_int}, {end_date_int})")
            cursor.execute(query, (start_date_int, end_date_int))
            results = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            cursor.close()
            connection.close()
            print("Connection closed.")

            if not results:
                print("No records found within the specified date range.")
                return Response({"message": "No data found."}, status=status.HTTP_204_NO_CONTENT)

            # Use multiprocessing to process rows
            with Pool(processes=cpu_count()) as pool:
                results_dict = pool.starmap(row_to_dict, [(row, columns) for row in results])

            print(f"Results: {results_dict}")

            metadata = {
                'icon': 'process.png',
                'persian': 'نمودار های یک ساعنه - میله ای',
                'report_type': 'chart_view',
                'chart_type': 'bar',
                'table': table,
                'x_axis': 'date',
                'y_axis': 'v24',
                'function': 'sum',
                'order_by': 'date',
                'y_axis_title': 'تن',
            }

            # Check if 'page' or 'page_size' is in query parameters
            page = request.query_params.get('page')
            page_size = request.query_params.get('page_size')

            if page or page_size:
                paginator = self.pagination_class()
                paginated_results = paginator.paginate_queryset(results_dict, request)
                response_data = {
                    'metadata': metadata,
                    'results': paginated_results,
                }
                return paginator.get_paginated_response(response_data)
            else:
                # Return all results if no pagination parameters are provided
                response_data = {
                    'metadata': metadata,
                    'results': results_dict,
                }
                return Response(response_data, status=status.HTTP_200_OK)

        except Exception as error:
            print(f"Error: {error}")
            return Response({"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChartDataViewHaftegiChart4Data(APIView):
    pagination_class = CustomPageNumberPagination

    def get(self, request, *args, **kwargs):
        dbConnectInfo = database.database_connection()
        try:
            connection = psycopg2.connect(dbConnectInfo)
            print("Connection to the database was successful.")
            cursor = connection.cursor()

            # Extract query parameters
            start_date_1 = request.query_params.get('start_date_1')
            end_date_1 = request.query_params.get('end_date_1')
            start_date_2 = request.query_params.get('start_date_2')
            end_date_2 = request.query_params.get('end_date_2')

            if not start_date_1 or not end_date_1:
                return Response({"error": "Both start_date_1 and end_date_1 are required"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                # Convert dates from "YYYY-MM-DD" to "YYYYMMDD" integer format
                def format_date(date_str):
                    return int(date_str.replace("-", ""))

                start_date_1 = format_date(start_date_1)
                end_date_1 = format_date(end_date_1)
                if start_date_2 and end_date_2:
                    start_date_2 = format_date(start_date_2)
                    end_date_2 = format_date(end_date_2)
            except ValueError:
                return Response({"error": "Dates must be in the format YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

            # Construct date range conditions dynamically
            date_conditions = ["(date >= %s AND date <= %s)"]
            parameters = [start_date_1, end_date_1]

            if start_date_2 and end_date_2:
                date_conditions.append("(date >= %s AND date <= %s)")
                parameters.extend([start_date_2, end_date_2])

            # Combine date range conditions
            date_condition_sql = " OR ".join(date_conditions)

            # SQL query with custom filtering logic
            raw_sql = f"""
                WITH t1 AS (
                    SELECT MAX(date) AS date
                    FROM tdd
                    WHERE tdd.type='mahshahr'
                      AND tdd.fluid='C4'
                      AND ({date_condition_sql})
                )
                SELECT 'موجودی مخازن بوتان ماهشهر' AS title, SUM(tdd.tonage) AS value
                FROM tdd
                JOIN tpv ON tdd.date = tpv.date AND tdd.tk = tpv.tk
                JOIN t1 ON tdd.date = t1.date
                WHERE tdd.type='mahshahr' 
                  AND tdd.fluid='C4'
                UNION
                SELECT 'ظرفیت خالی مخازن', SUM(tpv.max) - SUM(tdd.tonage)
                FROM tdd
                JOIN tpv ON tdd.date = tpv.date AND tdd.tk = tpv.tk
                JOIN t1 ON tdd.date = t1.date
                WHERE tdd.type='mahshahr'
                  AND tdd.fluid='C4';
            """

            # Execute the query
            print(f"Executing query: {raw_sql} with params {parameters}")
            cursor.execute(raw_sql, parameters)
            results = cursor.fetchall()

            # Fetch column names and build results
            columns = [desc[0] for desc in cursor.description]
            results_dict = [dict(zip(columns, row)) for row in results]

            cursor.close()
            connection.close()
            print("Connection closed.")

            # Metadata for the response
            metadata = {
                'persian': 'نمودار مخازن پروپان ماهشهر',
                'icon': 'process.png',
                'report_type': 'chart_view',
                'chart_type': 'pie',
                'x_axis': 'title',
                'y_axis': 'value',
                'function': 'sum',
                'order_by': 'title',
                'y_axis_title': 'تن',
            }

            # Paginate results if page and page_size are provided
            page = request.query_params.get('page')
            page_size = request.query_params.get('page_size')

            if page or page_size:
                paginator = self.pagination_class()
                paginated_results = paginator.paginate_queryset(results_dict, request)
                response_data = {
                    'metadata': metadata,
                    'results': paginated_results,
                }
                return paginator.get_paginated_response(response_data)
            else:
                # Return all results if no pagination parameters are provided
                response_data = {
                    'metadata': metadata,
                    'results': results_dict,
                }
                return Response(response_data, status=status.HTTP_200_OK)

        except Exception as error:
            print(f"Error: {error}")
            return Response({"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
