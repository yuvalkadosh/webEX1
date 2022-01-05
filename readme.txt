Please install:

pip install django==3.2.9
pip install django-axes
pip install django-sslserver
pip install django-widget-tweaks

to run:
python manage.py runsslserver --key .\key.pem --certificate .\cert.pem



מימוש SQL injection:
נרשום בשורת חיפוש:
' or 1=1--
וזה יציג לנו את כל המוצרים שקיימים בDB.

מימוש SQLI נוסף - בעמוד signup:
נרשום בתיבת username את הפקודה הבאה:
' union select id,password from auth_user where username = 'admin'-- - ASFSA
נלחץ create an account ונקבל את הHASH של המשתמש admin

מימוש XSS:
נלך ל-products&services
ניכנס למשל ל iphone 13 Pro ויקפצו לנו הודעות עם המילה 1/Hello כי רשמנו בתגובות:
<script> alert('1') </script>
<script> alert('Hello') </script>

מימוש נוסף:
נתחבר עם המשתמש :
<script>alert("hello")</script>
סיסמא:
Aa12345678

וכאשר נתחבר/נעבור בין העמודים השונים/נרענן את העמוד תקפץ לנו ההודעה hello כי העמוד כל פעם קורא את הסקריפט (השם משתמש)