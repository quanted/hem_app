from django.test import TestCase


class TestCalls(TestCase):
    """ testing that the pages exist and reply with 200 OK """
    def test_call_hem_landing_anonymous(self):
        response = self.client.get("/hem/popgen/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hem_index.html")

    def test_call_results_anonymous(self):
        response = self.client.get("/hem/results/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hem_results.html")