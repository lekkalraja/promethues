## Client Libraries

* Using client libraries, with usually adding two or three lines of code, you add your desired instrumentations to your code and define custom metric to be exposed.
* There are a number of client libraries available for all the major languages and runtimes.
* Prometheus project officially provides client libraries in Go, Java/Scala, Python and Ruby.
* Unofficial third-party client libraries : Bash, C, C++, PHP and more.
* Client Libraries take care of all the bookkeeping and producing the Prometheus format metrics.

#### Metric Types
- `Counter`
  * A counter is a cumulative metric that represents a single monotonically increasing counter whose value can only increase or it can be reset to zero on restart
  * Counters are mainly used to track how often a particular code path is executed
  * For Ex: Use counters to represent the number of requests served, tasks completed or errors.
  * Counters have one main method : `inc(amount int)` that increases the counter value `by default 1`
  * Do not use the counters to expose a value that can decrease
    * Ex: Temperature, the number of currently running processes, etc...

- `Gauge`
  * A gauge is a metric that represents a single numberical value that can arbitarily go up and down.
  * Gauges represent a snapshot of some current state.
  * For ex: Used for measured values like temperature, current memory usage, or anything whose value can go both up and down
  * Gauges have `inc(), dec(), set(), inc(amount), dec(amount)` that increases/decreases value by on and set the gauge to an arbitary value respectively.

- `Summary`
  * A summary samples observations like request durations - how long your application took to respond to a request, latency and request sizes.
  * Summarys track the size and number of events
  * Summary has one primary method `observe()` to which we pass the size of the event.
  * Summary exposes multiple time series during a scrape
    * The `total sum (<basename>_sum)` of all observed values
    * The `count (<basename>_count)` of events that have been observed
  * Summary metrics may also include quantiles over a sliding time window.


- `Histogram`
* A histogram samples observations (usually things like request durations or response sizes) and counts them in `configurable buckets`
* The instrumentation for histograms is the same as for Summary.
* Histogram exposes multiple time series during a scrape
  * The `total sum (<basename>_sum)` of all observed values
  * The `count (<basename>_count)` of events that have been observed
* The main purpose of using Histogram is calculating quantiles.

* For More Info : https://prometheus.io/docs/instrumenting/clientlibs/