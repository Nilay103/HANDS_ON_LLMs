from transformers import pipeline

summerizer = pipeline(task="summarization", model="facebook/bart-base")

text = """
High percentiles become especially important in backend services that are called mul‐
tiple times as part of serving a single end-user request. Even if you make the calls in
parallel, the end-user request still needs to wait for the slowest of the parallel calls to
complete. It takes just one slow call to make the entire end-user request slow, as illus‐
trated in Figure 1-5. Even if only a small percentage of backend calls are slow, the
chance of getting a slow call increases if an end-user request requires multiple back‐
end calls, and so a higher proportion of end-user requests end up being slow (an
effect known as tail latency amplification [24]).
If you want to add response time percentiles to the monitoring dashboards for your
services, you need to efficiently calculate them on an ongoing basis. For example, you
may want to keep a rolling window of response times of requests in the last 10
minutes. Every minute, you calculate the median and various percentiles over the val‐
ues in that window and plot those metrics on a graph.
The naïve implementation is to keep a list of response times for all requests within the
time window and to sort that list every minute. If that is too inefficient for you, there
are algorithms that can calculate a good approximation of percentiles at minimal
CPU and memory cost, such as forward decay [25], t-digest [26], or HdrHistogram
[27]. Beware that averaging percentiles, e.g., to reduce the time resolution or to com‐
bine data from several machines, is mathematically meaningless—the right way of
aggregating response time data is to add the histograms [28].
"""

print(summerizer(text)[0]["summary_text"])
