class AuthToken {
  final String access;
  final String refresh;

  AuthToken({required this.access, required this.refresh});

  factory AuthToken.fromJson(Map<String, dynamic> json) {
    return AuthToken(
      access: json['access'],
      refresh: json['refresh'],
    );
  }
}
