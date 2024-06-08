from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ScrapingJob
from .serializers import ScrapingJobSerializer
from .tasks import scrape_coin_data

class StartScrapingView(APIView):
    def post(self, request):
        coin_acronyms = request.data.get('coins', [])
        job = ScrapingJob.objects.create()
        scrape_coin_data.delay(job.job_id, coin_acronyms)
        return Response({"job_id": job.job_id}, status=status.HTTP_202_ACCEPTED)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        try:
            job = ScrapingJob.objects.get(job_id=job_id)
        except ScrapingJob.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ScrapingJobSerializer(job)
        return Response(serializer.data)
