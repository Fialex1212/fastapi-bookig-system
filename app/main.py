from fastapi import FastAPI, BackgroundTasks
from app.routers import event
from app.database import Base, engine
from app.confing import MailBody
from app.features.email_sender import send_mail

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(event.router, tags=["Events"])


@app.get("/")
def root():
    return "Home page"

@app.post("/send-email/")
async def send_email_endpoint(email: MailBody):
    send_mail(email.email, email.subject, email.message)
    return {"message": "Email sent successfully"}