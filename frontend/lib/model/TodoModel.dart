
class Todo {
  final int id;
  final int user;
  final String title;
  final bool completed;
  final DateTime createdAt;

  Todo({
    required this.id,
    required this.user,
    required this.title,
    required this.completed,
    required this.createdAt,
  });

  /// Convert JSON → Dart object
  factory Todo.fromJson(Map<String, dynamic> json) {
    return Todo(
      id: json['id'] as int,
      user: json['user'] as int,
      title: json['title'] as String,
      completed: json['completed'] as bool,
      createdAt: DateTime.parse(json['created_at']),
    );
  }

  /// Convert Dart object → JSON
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'user': user,
      'title': title,
      'completed': completed,
      'created_at': createdAt.toIso8601String(),
    };
  }
}
