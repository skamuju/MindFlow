## React Native
#### General Information
- Written in Javascript
- Best to combine with Express for server

#### Example of Code for Text
```js
const FlatListBasics = () => {
  return (
    <View style={styles.container}>
      <FlatList
        data={[
          {key: 'Devin'},
          {key: 'Dan'},
          {key: 'Dominic'},
          {key: 'Jackson'},
          {key: 'James'},
          {key: 'Joel'},
          {key: 'John'},
          {key: 'Jillian'},
          {key: 'Jimmy'},
          {key: 'Julie'},
        ]}
        renderItem={({item}) => <Text style={styles.item}>{item.key}</Text>}
      />
    </View>
  );
};

```
#### Pros
- Already familiar with React/Javascript/Typescript
- Cross-platform
- Many big companies use it (Meta, Microsoft, Amazon)
- Uses native operating system components from iOS and Android

#### Cons
- Slower than Flutter in general since it's not native
- Dependencies can get messy 


## Flutter
#### General Information
- Written primarily in C/C++
- Uses Google's Firebase application in backend (works best with Firebase as the database)
- Uses widgets to display components

#### Example of Code for ListView widget

```cpp
ListView(
  padding: const EdgeInsets.all(8),
  children: <Widget>[
    Container(
      height: 50,
      color: Colors.amber[600],
      child: const Center(child: Text('Entry A')),
    ),
    Container(
      height: 50,
      color: Colors.amber[500],
      child: const Center(child: Text('Entry B')),
    ),
    Container(
      height: 50,
      color: Colors.amber[100],
      child: const Center(child: Text('Entry C')),
    ),
  ],
)
```

#### Pros
- Faster/performs better since it's a compiled language
- Material UI components which provides more consistent experience
- Better for apps that need higher performance (animations)

#### Cons
- Not familiar with coding language (Dart)
- Flutter set-up is a little more work (needed to download from website and)
- Lack of third-party libraries
- Better for Android than IOS (most people have iPhones...)