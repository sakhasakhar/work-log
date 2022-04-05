from data import db_session
from data.jobs import Jobs
import datetime

db_session.global_init("db/blogs.db")


db_sess = db_session.create_session()
job = Jobs()
job.team_leader = 1
job.job = "ccccccccccc3"
job.work_size = 0
job.start_date = datetime.datetime.now()
job.collaborators = "2"
job.is_finished = True
db_sess.add(job)
db_sess.commit()
