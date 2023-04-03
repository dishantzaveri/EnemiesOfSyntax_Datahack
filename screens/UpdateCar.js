import { View, Text, TextInput, Button, StyleSheet, TouchableOpacity, Image, Alert, ScrollView, SafeAreaView,Pressable } from 'react-native'
import React, { useState } from 'react'

export default function UpdateCar() {
    const [brand, setBrand] = useState("");
    const [transmissionType, setTransmissionType] = useState("");
    const [fuelType, setFuelType] = useState("");
    const [color, setColor] = useState("");
    const [price, setPrice] = useState("");
    const [open, setOpen] = useState(false)

    return (
        <SafeAreaView style={{ flex: 1,backgroundColor:'black' }}>
            <ScrollView>
                <View style={styles.container}>
                    <Text style={{ fontSize: 20, justifyContent: 'center', color: "white", fontWeight: 'bold', paddingTop: '10%', fontFamily: 'Roboto',alignContent:'center',alignSelf:'center',alignItems:'center' }}>Update Information</Text>

                    {/* <TextInput style={styles.input1} placeholder='Image' value={brand} onChangeText={(e) => { setBrand(e) }} /> */}
                    <TextInput style={styles.input2} placeholder='Km Driven' value={transmissionType} onChangeText={(e) => { setTransmissionType(e) }} />
                    <TextInput style={styles.input2} placeholder='Model car' value={fuelType} onChangeText={(e) => { setFuelType(e) }} />
                    <TextInput style={styles.input2} placeholder='Engine Size' value={color} onChangeText={(e) => { setColor(e) }} />
                    <TextInput style={styles.input2} placeholder='Year' value={price} onChangeText={(e) => { setPrice(e) }} />

                    <Pressable
                  style={[styles.button, styles.buttonClose]}
                >
                  <Text style={styles.textStyle}>Update</Text>
                </Pressable>
                </View>
            </ScrollView>
        </SafeAreaView>
    )
}

const styles = StyleSheet.create({
    container: {
        justifyContent: 'center',
        alignItems: 'center'
    },
    input1: {
        marginTop: '15%',
        borderWidth: 1,
        padding: 10,
        width: '80%',
        borderRadius: 10,
        fontFamily: 'normal',
        backgroundColor: 'white',

    },
    input2: {
        marginTop: '3%',
        borderWidth: 1,
        padding: 10,
        width: '80%',
        borderRadius: 10,
        fontFamily: 'normal',
        backgroundColor: 'white',
    },
    button: {
        borderRadius: 10,
        padding: 10,
        elevation: 2,
        marginTop: '10%',
        width: '50%',
        padding: 5,
        height: 45,
        borderRadius: 15
      },
      buttonOpen: {
        backgroundColor: "#2196F3",
      },
      buttonClose: {
        backgroundColor: "green",
      },
      buttonExit: {
        backgroundColor: "red",
      },
      textStyle: {
        color: "white",
        fontWeight: "bold",
        textAlign: "center",
        fontSize:20,
        marginTop: '2%',
      },
      modalText: {
        marginBottom: 15,
        textAlign: "center"
      },
})