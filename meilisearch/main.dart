import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Flutter Demo',
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final List<int> l = [1, 2, 4, 5, 3, 1, 6, 57, 8, 3, 4, 65];
  final TextEditingController _controller = TextEditingController();
  int _index = 0;

  void _showValues() {
    setState(() {
      _index = int.tryParse(_controller.text) ?? 0;
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('显示输入内容'),
      ),
      body: Column(
        children: [
          TextField(
            controller: _controller,
            keyboardType: TextInputType.number,
            decoration: const InputDecoration(
              labelText: '输入索引：',
            ),
            onChanged: (_) => _showValues(),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: l.length - _index,
              itemBuilder: (BuildContext context, int index) {
                return Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Text(l[_index + index].toString()),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}
