import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class Securestorage {
  final _storage= FlutterSecureStorage();

   //! SAVE THE TOKEN 
   Future<void>savetoken(String assessToken,String refreshToken)async{
    await _storage.write(key: "accessToken", value: assessToken);
    await _storage.write(key: "refreshToken", value: refreshToken);
   

   }

   //! READ THE TOKEN

   Future<String?> getAccessToken() async => _storage.read(key: "accessToken");
  Future<String?> getRefreshToken() async => _storage.read(key: "refreshToken");


    //! DELETE THE 
    Future<void>deleted()async=>await _storage.deleteAll();



    
     
}