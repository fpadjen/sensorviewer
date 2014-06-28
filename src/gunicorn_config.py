import os
import multiprocessing

bind = "0.0.0.0:{}".format(os.getenv("PORT", 5000))
# size = int(os.getenv("SIZE", 1))
# Maximum 5 worker per 128MB
# workers = min(multiprocessing.cpu_count() * 2 + 1, size * 5)
workers = 4
timeout = 120
