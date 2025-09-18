import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

import 'package:todo/auth/ui/LoginPage.dart';



void main() {
  runApp(ProviderScope(child: const MyApp()));
}

class MyApp extends ConsumerWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context , WidgetRef ref) {
    return ScreenUtilInit(
      designSize: Size(360, 640), 
      minTextAdapt: true,
      splitScreenMode: true,
      builder: (context, child) {

        return MaterialApp(
          debugShowCheckedModeBanner: false,
          home: Loginpage(),
        );
      },
      
    );
  }
}

