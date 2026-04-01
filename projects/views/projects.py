from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from projects.models import Project
from projects.serializers import ProjectListSerializer, ProjectCreateSerializer


class ProjectListCreateApiView(APIView):
    def parse_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return None

    def get(self, request: Request) -> Response:
        all_projects = Project.objects.all()

        date_from = request.query_params.get("date_from")
        date_to = request.query_params.get("date_to")

        # if date_from and date_to:
        #     parsed_date_from = self.parse_date(date_from)
        #     parsed_date_to = self.parse_date(date_to)

        #     if parsed_date_from is None or parsed_date_to is None:
        #         return Response(
        #             data={'date_from': ['Invalid date format.'], 'date_to': ['Invalid date format.']},
        #             status=status.HTTP_400_BAD_REQUEST
        #         )

        #     if parsed_date_from > parsed_date_to:
        #         return Response(
        #             data={'date_from': ['Date from must be less than date to.']},
        #             status=status.HTTP_400_BAD_REQUEST
        #         )

        #     all_projects = all_projects.filter(created_at__range=[parsed_date_from, parsed_date_to])
        if date_from:
            parsed_date_from = self.parse_date(date_from)
            if parsed_date_from is None:
                return Response(
                    data={"date_from": ["Invalid date format."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            all_projects = all_projects.filter(created_at__gte=parsed_date_from)
        if date_to:
            parsed_date_to = self.parse_date(date_to)
            if parsed_date_to is None:
                return Response(
                    data={"date_to": ["Invalid date format."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            all_projects = all_projects.filter(created_at__lte=date_to)

        serializer = ProjectListSerializer(all_projects, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = ProjectCreateSerializer(data=request.data)

        if serializer.is_valid():
            project = serializer.save()
            response_serializer = ProjectListSerializer(project)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def get_all_projects(request: Request) -> Response:
#     if request.method == 'GET':
#         all_projects = Project.objects.all()

#         date_from = request.query_params.get('date_from')
#         date_to = request.query_params.get('date_to')

#         if date_from and date_to:
#             try:
#                 parsed_date_from = datetime.strptime(date_from, '%Y-%m-%d').date()
#                 parsed_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
#             except ValueError:
#                 return Response(
#                     data={'date_from': ['Enter date in YYYY-MM-DD format.'], 'date_to': ['Enter date in YYYY-MM-DD format.']},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             if parsed_date_from > parsed_date_to:
#                 return Response(
#                     data={'date_from': ['Date from must be less than date to.']},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             all_projects = all_projects.filter(created_at__range=[parsed_date_from, parsed_date_to])
#         # elif date_from:
#         #     parsed_date_from = datetime.strptime(date_from, '%Y-%m-%d').date()
#         #     all_projects = Project.objects.filter(created_at__gte=date_from)
#         # elif date_to:
#         #     parsed_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
#         #     all_projects = Project.objects.filter(created_at__lte=date_to)


#         serializer = ProjectListSerializer(all_projects, many=True)

#         return Response(
#             data=serializer.data,
#             status=status.HTTP_200_OK
#         )
#     elif request.method == 'POST':
#         serializer = ProjectCreateSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 data=serializer.data,
#                 status=status.HTTP_201_CREATED
#             )
#         else:
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
