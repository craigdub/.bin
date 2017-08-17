import React, { Component } from 'react';
import {
  Button,
  Image,
  StyleSheet,
  Text,
  TextInput,
  TouchableHighlight,
  ScrollView,
  View,
} from 'react-native';

import { CheckBox } from 'react-native-elements'


class App extends React.Component {
  static navigationOptions = ({ navigation, screenProps }) => ({
    title: 'Explore',
  });

  render() {
    return (
      <ScrollView contentContainerStyle={styles.container}>
        <Text>You did it!</Text>
      </ScrollView>
    );
  }
}

export default App;

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
});
