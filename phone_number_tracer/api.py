from rest_framework.views import APIView
from django.conf import settings
from services.place import get_place_ids, get_phone_number_from_place_id
from rest_framework.response import Response
from rest_framework import status


class GetPhoneNumber(APIView):
    """Get Phone Number"""

    def get(self, request, *args, **kwargs):
        address = request.query_params.get("address")
        if address is not None:
            try:
                place_ids = get_place_ids(address)
                results = []
                for place_id in place_ids:
                    results.append(get_phone_number_from_place_id(place_id))
                return Response({"results": results})
            except Exception as e:
                return Response(
                    {"error": f"Error has occurred! {e}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        # else:
        return Response(
            {"error": "Address is required!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
