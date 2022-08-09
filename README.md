# Üniversite Öğrenci Bilgi Sistemi - University Student Information System

Bu proje python django kullanılarak yazılmış bir üniversite öğrenci bilgi sistemidir. Projedeki asıl amaç öğrencilerle bölüm arasında bir köprü kurmak ve öğrenciler mezun olduktan sonra da bu ilişkiyi devam ettirebilmektir. Sistemde öğrenci, mezun, öğretim görevlisi, bölüm sekreteri ve admin olmak üzere beş giriş vardır.

Sistemde; 

  -> Öğrenci olan kullanıcılar için diğer öğrencilerle paylaşacağı ders notu ekleme, sınav sonuçlarını görüntüleme, öğretim görevlisinden görüşme için randevu talep etme, bölüm sekreterinden belge talep etme, sisteme eklenen iş ve staj ilanlarını görüntüleme gibi modüller bulunmaktadır.

  -> Mezun olan kullanıcılar için öğretim görevlisinden görüşme için randevu talep etme, bölüm sekreterinden belge talep etme, sisteme eklenen iş ilanlarını görüntüleme ve sisteme iş ve staj ilanları ekleme gibi modüller bulunmaktadır.

  -> Öğretim görevlisi olan kullanıcılar için öğrencilerle paylaşacağı ders notu ekleme, sınav sonuçları ekleme, gelen randevu taleplerini değerlendirme, iş ve staj ilanları ekleme gibi modüller bulunmaktadır.

  -> Bölüm sekreteri olan kullanıcılar için öğrencilerden gelen belge taleplerini değerlendirme ve belge gönderme gibi modüller bulunmaktadır.

  Ayrıca sistemde kayıtlı kullanıcılardan elde edilen bilgilerle oluşturulan site içi bilgi grafileri bulunmaktadır. Yine sistemdeki kullanıcıların yaşı, mezuniyet tarihi, mezuniyet ortalaması, maaşı ve yaşadığı şehir gibi bilgiler kullanılarak regresyon analizi gerçekleştirilmiştir. Regresyon analizi sonucunda girilen bilgiler için tahmini işe başlama süresi ve tahmini maaş gibi bilgiler gösterilerek öğrencilerin gelecekteki kariyerleri hakkında bilgi sahibi olmaları amaçlanmıştır.
  

This project is a university student information system written using python django. The main purpose of the project is to build a bridge between the students and the department and to maintain this relationship after the students graduate. There are five login in the system: student, alumni, lecturer, department secretary and admin.

In the system;

  -> For users who are students, there are apps such as adding lecture notes to share with other students, viewing exam results, requesting an appointment from the lecturer for an meeting, requesting documents from the department secretary, viewing job and internship postings added to the system.
  
  -> For graduate users, there are apps such as requesting an appointment from the lecturer for an meeting, requesting documents from the department secretary, viewing job postings added to the system, and adding job and internship postings to the system.
  
  In addition, there are in-site infographics created with the information obtained from registered users in the system. Again, regression analysis was carried out by using information such as the age, graduation date, graduation average, salary and city of residence of the users in the system. For the information entered as a result of the regression analysis, it is aimed to inform the students about their future careers by showing information such as estimated starting time and estimated salary.
  
  -> For users who are lecturers, there are apps such as adding lecture notes to share with students, adding exam results, evaluating incoming appointment requests, adding job and internship postings to the system.
  
  -> For users who are department secretaries, there are apps such as evaluating document requests from students and sending documents.
