import 'dart:developer';
import 'package:dio/dio.dart';





class Authrepo {

  final dio = Dio(
    BaseOptions(
    //  baseUrl: "http://10.44.222.251:8000/",
      connectTimeout: Duration(seconds: 5),
      receiveTimeout: Duration(seconds: 5),
      headers: {"Content-Type": "application/json"},
    ),
  );
  


  Future<Map<String, dynamic>> signup(String email, String password, String username) async {
    try {
      final response = await dio.post(
           "http://10.44.222.251:8000/singup/",
        data: {"email": email, "password": password, "username": username},
      );
      return {"success": true, "data": response.data};
    } on DioException catch (e) {
      log(e.toString());
      return {
        "success": false,
        "error": e.response?.data ?? e.message,
        
      };
    
    }
  }
}

