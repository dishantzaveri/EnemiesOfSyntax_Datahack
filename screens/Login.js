import { View, Input, FlatList, Text, TextInput, Button, StyleSheet, TouchableOpacity, Image, ImageBackground, Alert, ScrollView, SafeAreaView } from 'react-native'
import React, { useState, useEffect } from 'react'
import { Divider } from "@react-native-material/core";
import LottieView from 'lottie-react-native';


export default function Login({ navigation }) {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  loginUser = () => {
    if (username != "" && password != "") {
      fetch(`http://192.168.8.109:8000/users/login/${username}/${password}`, {
        method: "GET",
        headers: {
          'content-type': 'application/json'
        }
      })
        .then((response) => response.json())
        .then((json) => {
          console.log(json);
          if (json.length === 0) {
            Alert.alert("Username or password incorrect.Try again!")
          } else {
            clearTextFields()
            Alert.alert("Login Successful.");
            navigation.navigate("DashBoard")
          }
        })
        .catch((err) => console.log(err));
    } else {
      Alert.alert("Please Enter Username and password and try again.")
    }
  }

  clearTextFields = () => {
    setUsername("");
    setPassword("");
  }


  return (
    <SafeAreaView style={{ flex: 1,backgroundColor: '#000000' }}>
      <ScrollView>
        <View style={styles.container} >
          <Text style={{ fontSize: 35, justifyContent: 'center', color: "white", fontWeight: 'bold', paddingTop: '15%', fontFamily: 'Roboto' }}>Welcome</Text>
          <LottieView
            source={require('./car.json')}
            autoPlay={true}
            loop={false}

            style={styles.animation}
          />
          <TextInput style={styles.input1} value={username} onChangeText={(e) => { setUsername(e) }} placeholder='Username' />
          <TextInput style={styles.input2} value={password} onChangeText={(e) => { setPassword(e) }} placeholder='Password' />


          <TouchableOpacity
            style={styles.btn}
            onPress={() => { navigation.navigate("DashBoard") }}
          // onPress={() => { loginUser() }}
          // onPress={() => { loginUser() }} 
          >
            <Text style={{ color: '#ffff', fontSize: 20 }}>Login</Text>
          </TouchableOpacity>
          <Text style={{ fontSize: 18, color: "white", paddingTop: '8%', left: '-13%' }}>Don't have an account?</Text>
          <TouchableOpacity
            style={styles.btn2}
            onPress={() => {
              try {
                navigation.navigate("Register")
              } catch (err) {
                console.log(err);
              }
            }}
          >
            <Text style={{ color: 'white', fontSize: 18, fontWeight: 'bold' }}>Create One</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  input1: {
    marginTop: '10%',
    borderWidth: 1,
    padding: 10,
    width: '80%',
    borderRadius: 15,
    backgroundColor: 'white',
    fontFamily: 'Roboto'


  },
  input2: {
    marginTop: '5%',
    borderWidth: 1,
    padding: 10,
    width: '80%',
    borderRadius: 15,
    backgroundColor: 'white',
    fontFamily: 'Roboto'
  },
  container: {
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#000000',
    flex: 1,

  },
  btn: {
    width: '80%',
    padding: 5,
    backgroundColor: "#055BC7",
    height: 50,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: '5%',
    borderRadius: 15,

  },
  animation: {
    width: 150,
    height: 200,
    margin: 25,
    marginLeft: 20,
    alignContent: 'center',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: '5%'
  },
  btn2: {
    width: '60%',
    padding: 5,
    // backgroundColor: "#0EAF52",
    height: 50,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: '-10%',
    marginLeft: '55%',
    borderRadius: 100
  },
  tinyLogo: {
    marginTop: '10%',
    width: 100,
    height: 100,
  }
});