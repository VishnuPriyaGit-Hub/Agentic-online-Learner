# Agentic-online-Learner
The agent’s goal is to provide personalized learning, assessment, and progress tracking for school students, subject to curriculum standards, teaching rules, and role-based access, while optimizing for student learning mastery, teacher efficiency, and clear visibility for parents 

## Problem Context 

School students, teachers, and parents face difficulties because learning is not personalized. Today, teaching follows a fixed syllabus and pace for all students, even though students learn at different speeds. Teachers spend a lot of time creating lesson plans, tests, and feedback manually, which can be tiring and inconsistent. Students often receive general or late feedback, so they do not clearly understand their mistakes or learning gaps. Parents mostly rely on report cards, which are infrequent and do not show detailed progress. This manual system is slow, hard to scale, increases teacher workload, and does not give timely insights. 
 

## Scope and Boundaries 

  Actions the agent is allowed to take 

  ### Student-related actions 

  Create personalized learning content based on the curriculum 

  Adjust difficulty and pace based on student level 

  Give practice questions, quizzes, hints, and explanations 

  Track learning progress and mastery levels 

### Teacher-related actions 

  Suggest lesson plans and topic order 

  Create draft assessments and rubrics 

  Analyze student performance and learning gaps 

  Suggest feedback and improvement actions 

### Parent-related actions 

  Show simple progress summaries 

  Highlight strengths and improvement areas 

  Recommend next learning steps 

### System-level actions 

  Maintain topic relationships and prerequisites 

  Track learning effectiveness 

  Ensure privacy and safety 

 

### When the agent must stop and ask a human (HITL)

  Before final exams or assessments 

  When changing curriculum or grading rules 

  If a student is not improving and needs intervention 

  Before generating final evaluation reports 

  When content accuracy is uncertain 

 

## Out-of-scope decisions 

Giving final grades or promotions 

Overriding teacher-defined rules 

Diagnosing learning or psychological disorders 

Comparing students or ranking them 

Making payment, legal, or disciplinary decisions 

 

## User Types 

Who interacts with the agent? 

Students – learn topics, attempt assessments, get feedback 

Teachers – plan lessons, review performance, guide students 

Parents – monitor learning progress 

How does the interaction begin? 

Student logs in and selects a subject or topic 

Teacher opens a course or class dashboard 

Parent checks the progress dashboard or summary 

 

## Formal Conversation Samples 

Conversation 1: Student Learning and Assessment 

Student: 
“I want to learn fractions. I find word problems hard.” 

Agent: 
“Let me give you a short quiz to understand your level.” 

(Student completes quiz) 

Agent: 
“You understand basic fractions, but word problems are difficult. Let’s practice with simple step-by-step examples.” 

(Practice questions provided) 

Agent: 
“You are improving. Your mastery increased from 45% to 70%. Would you like to try a harder problem or revise again?” 

Goal achieved: Personalized learning, assessment, and progress tracking completed.  
