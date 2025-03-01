"""resiliencehub base URL and path."""
from .responses import ResilienceHubResponse

url_bases = [
    r"https?://resiliencehub\.(.+)\.amazonaws\.com",
]

url_paths = {
    "{0}/create-app$": ResilienceHubResponse.dispatch,
    "{0}/create-resiliency-policy$": ResilienceHubResponse.dispatch,
    "{0}/describe-app$": ResilienceHubResponse.dispatch,
    "{0}/describe-resiliency-policy$": ResilienceHubResponse.dispatch,
    "{0}/list-apps$": ResilienceHubResponse.dispatch,
    "{0}/list-app-assessments$": ResilienceHubResponse.dispatch,
    "{0}/list-resiliency-policies$": ResilienceHubResponse.dispatch,
    "{0}/tags/.+$": ResilienceHubResponse.dispatch,
    "{0}/tags/(?P<arn_prefix>[^/]+)/(?P<workspace_id>[^/]+)$": ResilienceHubResponse.method_dispatch(
        ResilienceHubResponse.tags  # type: ignore
    ),
    "{0}/.*$": ResilienceHubResponse.dispatch,
}
