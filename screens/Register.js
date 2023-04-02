import { View, Text, TextInput, Button, StyleSheet, TouchableOpacity, Image, Alert, ScrollView, SafeAreaView } from 'react-native'
import React, { useState } from 'react';
import LottieView from 'lottie-react-native';


export default function Register({ navigation }) {

  const [fullName, setFullName] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const saveUser = async () => {

    if (fullName != "" && phoneNumber != "" && username != "" && password != "") {
      fetch('http://192.168.8.109:8000/users', {
        method: 'POST',
        body: JSON.stringify({
          fullName: fullName,
          phoneNumber: phoneNumber,
          username: username,
          password: password
        }),
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        },
      })
        .then((response) => response.json())
        .then((json) => {
          if (json.status === "500") {
            Alert.alert(json.message)
          } else {
            Alert.alert(json.message)
            clearTextFields();
          }
        })
        .catch((err) => Alert.alert(err.message));
    } else {
      Alert.alert("Please fill all the fields and try again.")
    }
  }


  const clearTextFields = () => {
    setFullName("");
    setPhoneNumber("");
    setUsername("");
    setPassword("");
  }


  return (
    <SafeAreaView style={{ flex: 1 ,backgroundColor:'#000000'}}>
      <ScrollView>
        <View style={styles.container}>
          <Text style={{ fontSize: 35, justifyContent: 'center', color: "white", fontWeight: 'bold', paddingTop: '10%', fontFamily: 'Roboto' }}>Create Account</Text>
          <LottieView
            source={require('./car.json')}
            autoPlay={true}
            loop={false}

            style={styles.animation}
          />
          <TextInput style={styles.input1} value={fullName} onChangeText={(e) => { setFullName(e) }} placeholder='Full Name' />
          <TextInput style={styles.input2} value={phoneNumber} onChangeText={(e) => { setPhoneNumber(e) }} placeholder='Phone Number' />
          <TextInput style={styles.input2} value={username} onChangeText={(e) => { setUsername(e) }} placeholder='Username' />
          <TextInput style={styles.input2} value={password} onChangeText={(e) => { setPassword(e) }} placeholder='Password' />
          <TouchableOpacity
            style={styles.btn}
            onPress={() => {
              saveUser()
              // printUser()
            }}
          >
            <Text style={{ color: '#ffff', fontSize: 20 }}>Register</Text>

          </TouchableOpacity>

          <Text style={{ fontSize: 18, color: "white", paddingTop: '8%', left: '-10%' }}>Already have an account?</Text>
          <TouchableOpacity
            style={styles.btn2}
            onPress={() => {
              try {
                navigation.navigate("Login")
              } catch (err) {
                console.log(err);
              }
            }}
          >
            <Text style={{ color: 'white', fontSize: 20, fontWeight: 'bold' }}>Login</Text>
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
    fontFamily: 'Roboto',
    backgroundColor: 'white',

  },
  input2: {
    marginTop: '5%',
    borderWidth: 1,
    padding: 10,
    width: '80%',
    borderRadius: 15,
    backgroundColor: 'white',
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
  container: {
    justifyContent: 'center',
    alignItems: 'center'
  },
  btn: {
    width: '80%',
    padding: 5,
    backgroundColor: "#055BC7",
    height: 50,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: '5%',
    borderRadius: 15
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
    marginTop: '5%',
    width: 70,
    height: 70,
  },

});