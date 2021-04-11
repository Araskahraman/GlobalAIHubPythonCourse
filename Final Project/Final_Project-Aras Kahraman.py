competition_questions= [
    "Türkiyenin başkenti neresidir?",
    "Python programını yazan kişinin adı nedir?",
    "Atatürk'ün doğum yeri neresidir?",
    "Atatürk'ün doğum tarihi nedir?",
    "Umman devleti hangi kıtada bulunur?",
    "Kimono hangi ülkeye ait geleneksel bir giysidir?",
    "2013-2014 yılı Türkiye Süper Lig şampiyonu hangi takımdır?",
    "Trakya bölgesi hangi kıtada bulunur",
    "Geleneksel Türk evlerinde bulunan üstüne çay gibi içeceklerin konulduğu küçük sehpanın adı nedir?",
    "Fransanın başkenti neresidir?",
    ]
competition_answers= ["Ankara","Guido","Selanik","1881","Asya","Japonya","Fenerbahçe","Avrupa","zigon","Paris"]


count = 0
for question,answer in zip(competition_questions,competition_answers):
    
    print(question)
        
    user_answer=str(input("Please enter your answer"))
    
    if user_answer == answer:
        print("Congrats, you've earn 10 points!")
        
        count += 10
        
    else:
        print("Wrong Answer")
        
if count >= 60:
    print("Congratulations! You have passed the competition!")
    
else:
    print("Unfortunately, you have lost the competition")
