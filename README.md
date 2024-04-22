
# Comparison of Beanstalkd and Redis for Message Queuing

| Queue | Message Size | Put (ms) | Put (req/s) | Get (ms) | Get (req/s) |
|-------|--------------|----------|-------------|----------|-------------|
| Beanstalkd | 28 bytes | 117.71 | 4246.77 | 235.89 | 2120.24 |
| Redis (rdb) | 28 bytes | 256.32 | 1950.23 | 203.47 | 2457.81 |
| Beanstalkd | 6800 bytes | 239.41 | 2088.44 | 558.93 | 895.09 |
| Redis (rdb) | 6800 bytes | 386.74 | 1292.85 | 383.36 | 1304.29 |
| Redis (aof) | 28 bytes | 415.56 | 1203.20 | 487.39 | 1025.71 |
| Redis (aof) | 6800 bytes | 679.51 | 736.14 | 520.52 | 960.40 |

### Based on the results shown in the table, we can make the following conclusions:

1. **Beanstalkd outperforms Redis for small messages (28 bytes):** For both putting and getting small messages, Beanstalkd has significantly higher requests per second (req/s) compared to Redis with either rdb or aof persistence.

2. **Redis (rdb) performs better than Beanstalkd for large messages (6800 bytes):** When dealing with large messages, Redis with rdb persistence has higher req/s for both putting and getting messages compared to Beanstalkd.

3. **Redis (aof) has the lowest performance:** Across all scenarios, Redis with aof persistence consistently has the lowest req/s for both putting and getting messages, whether small or large.

4. **Message size impacts performance:** The performance of both Beanstalkd and Redis is affected by the size of the messages being processed. For small messages, the req/s is higher than for large messages, which is expected as smaller messages require less overhead for processing.

In summary, for workloads involving small messages, Beanstalkd is the better choice due to its higher throughput. However, for workloads with large messages, Redis with rdb persistence offers better performance than Beanstalkd. The choice between Beanstalkd and Redis should be made based on the specific requirements of the application, considering factors such as message size, throughput requirements, and the need for persistence.