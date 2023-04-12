from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return f'{self.name} 전문의'
    
class Patient(models.Model):
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctors = models.ManyToManyField(Doctor, through='Reservation') # 닥터 필드랑 M:N 관계 
    name = models.TextField()
    
    
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
    
    
     
class Reservation(models.Model): # 중계 테이블
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'


