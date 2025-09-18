class UserModel {
  final int? id;            // Django auto id (if returned by API)
  final String username;
  final String email;
  final String? bio;
  final bool isActive;
  final bool isStaff;
  final String createdAt;

  UserModel({
    this.id,
    required this.username,
    required this.email,
    this.bio,
    required this.isActive,
    required this.isStaff,
    required this.createdAt,
  });

  // Convert JSON -> Dart Object
  factory UserModel.fromJson(Map<String, dynamic> json) {
    return UserModel(
      id: json['id'],
      username: json['username'],
      email: json['email'],
      bio: json['bio'],
      isActive: json['is_active'] ?? true,
      isStaff: json['is_staff'] ?? false,
      createdAt: json['created_at'] ?? "",
    );
  }

  // Convert Dart Object -> JSON (for POST/PUT requests)
  Map<String, dynamic> toJson() {
    return {
      "id": id,
      "username": username,
      "email": email,
      "bio": bio,
      "is_active": isActive,
      "is_staff": isStaff,
      "created_at": createdAt,
    };
  }
}
