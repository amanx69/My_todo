import 'dart:developer';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:todo/auth/riverpode/singup/Authrepo.dart';

// Provider for Authrepo
final provi = Provider<Authrepo>((ref) => Authrepo());

// --- State ---
class SignupState {
  final bool isLoading;
  final String? error;
  final bool isSuccessful;

  SignupState({
    this.isLoading = false,
    this.error,
    this.isSuccessful = false,
  });

  SignupState copyWith({
    bool? isLoading,
    String? error,
    bool? isSuccessful,
  }) {
    return SignupState(
      isLoading: isLoading ?? this.isLoading,
      error: error ?? this.error,
      isSuccessful: isSuccessful ?? this.isSuccessful,
    );
  }
}

// --- Notifier ---
class SignupNotifier extends StateNotifier<SignupState> {
  final Authrepo authrepo;
  SignupNotifier({required this.authrepo}) : super(SignupState());

  Future<void> signup(String email, String password, String username) async {
    // Start loading
    state = state.copyWith(isLoading: true, error: null, isSuccessful: false);

    final result = await authrepo.signup(email, password, username);

    if (result['success']) {
      state = state.copyWith(isLoading: false, isSuccessful: true);
    } else {
      state = state.copyWith(
        isLoading: false,
        error: result['error'].toString(),
        isSuccessful: false,
      );
      log("Signup failed: ${result['error']}");
    }
  }
}

// --- Provider for SignupNotifier ---
final signupProvider =
    StateNotifierProvider<SignupNotifier, SignupState>((ref) {
  return SignupNotifier(authrepo: ref.watch(provi));
});
