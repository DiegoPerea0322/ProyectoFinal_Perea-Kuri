# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Advisor(models.Model):
    s = models.OneToOneField('Student', models.CASCADE, db_column='s_ID', primary_key=True)
    i = models.ForeignKey('Instructor', models.SET_NULL, db_column='i_ID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advisor'

class Classroom(models.Model):
    building = models.CharField(primary_key=True, max_length=15)
    room_number = models.CharField(unique=True, max_length=7)
    capacity = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classroom'
        unique_together = (('building', 'room_number'),)

class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=8)
    title = models.CharField(max_length=50, blank=True, null=True)
    dept_name = models.ForeignKey('Department', models.SET_NULL, db_column='dept_name', blank=True, null=True)
    credits = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=20)
    building = models.CharField(max_length=15, blank=True, null=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.dept_name}"

    class Meta:
        managed = False
        db_table = 'department'


class Instructor(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=5)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    dept_name = models.ForeignKey(Department, models.SET_NULL, db_column='dept_name', blank=True, null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor'

    def __str__(self):
        return f"{self.id}"




class Prereq ( models.Model ):
    course_id = models.ForeignKey ( Course, on_delete=models.CASCADE, db_column='course_id',
                                    related_name='course_prereq' )
    prereq_id = models.ForeignKey ( Course, on_delete=models.CASCADE, db_column='prereq_id',
                                    related_name='prereq_prereq' )

    class Meta:
        managed = False
        db_table = 'prereq'
        unique_together = ('course_id', 'prereq_id')


class Section(models.Model):
    course = models.OneToOneField(Course, models.DO_NOTHING, primary_key=True)
    sec_id = models.CharField(unique=True,max_length=8)
    semester = models.CharField(unique=True,max_length=6)
    year = models.DecimalField(unique=True,max_digits=4, decimal_places=0)
    building = models.ForeignKey(Classroom, models.DO_NOTHING, db_column='building', blank=True, null=True, related_name='sections_in_building')
    room_number = models.ForeignKey(Classroom, models.DO_NOTHING, db_column='room_number', to_field='room_number', blank=True, null=True, related_name='sections_in_room')
    time_slot_id = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section'
        unique_together = (('course', 'sec_id', 'semester', 'year'),)

    # def __str__(self):
    #     return f"Section ID: {self.sec_id}, Course Name: {self.course}"
    #
    # def __repr__(self):
    #     return f"Section ID: {self.sec_id}, Course Name: {self.course}"



class Student(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=5)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    tot_cred = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Takes(models.Model):
    ID = models.ForeignKey(Student, models.DO_NOTHING, db_column='ID', related_name='takes_student')
    course_id = models.ForeignKey(Section, models.DO_NOTHING, db_column='course_id', to_field='course_id', related_name='takes_course')
    sec_id = models.ForeignKey(Section, models.DO_NOTHING,  unique=True,db_column='sec_id', to_field='sec_id', related_name='takes_sec')
    semester = models.ForeignKey(Section, models.DO_NOTHING,unique=True, db_column='semester', to_field='semester', related_name='takes_semester')
    year = models.ForeignKey(Section, models.DO_NOTHING,unique=True, db_column='year', to_field='year', related_name='takes_year')
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'takes'
        unique_together = (('ID', 'course_id', 'sec_id', 'semester', 'year'),)



class Teaches(models.Model):
    ID = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='ID', related_name='teaches_instructor')
    course_id = models.ForeignKey(Section, models.DO_NOTHING, db_column='course_id', to_field='course_id', related_name='teaches_course')
    sec_id = models.ForeignKey(Section, models.DO_NOTHING, db_column='sec_id', to_field='sec_id', related_name='teaches_sec')
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester', to_field='semester', related_name='teaches_semester')
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='year', to_field='year', related_name='teaches_year')

    class Meta:
        managed = False
        db_table = 'teaches'
        unique_together = (('ID', 'course_id', 'sec_id', 'semester', 'year'),)


class TimeSlot(models.Model):
    time_slot_id = models.CharField(primary_key=True, max_length=4)
    day = models.CharField(max_length=1)
    start_hr = models.DecimalField(max_digits=2, decimal_places=0)
    start_min = models.DecimalField(max_digits=2, decimal_places=0)
    end_hr = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    end_min = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_slot'
        unique_together = (('time_slot_id', 'day', 'start_hr', 'start_min'),)
