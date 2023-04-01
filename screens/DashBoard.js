import { View, Text, TextInput, Button, StyleSheet, TouchableOpacity, Image } from 'react-native'
import React, { useState } from 'react'
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import AddVehicle from '../screens/AddVehicle'
import VehicleInfo from '../screens/VehicleInfo'
import { IconComponentProvider, Icon } from "@react-native-material/core";
import { HomeStackNavigator, ContactStackNavigator } from "./StackNavigator";
import Home from './Home';
import UpdateCar from './UpdateCar';



const Tab = createBottomTabNavigator();

export default function DashBoard() {
  return (
    <Tab.Navigator screenOptions={{ headerShown: false }}>
      <Tab.Screen name="Home"
        options={{
          tabBarIcon: () => (<Image source={require("../assets/icon/home.png")} style={{ width: 20, height: 20 }} />), header: () => null
        }}
        component={Home} />

      <Tab.Screen name="Post"
        options={{
          tabBarIcon: () => (<Image source={require("../assets/icon/adding.png")} style={{ width: 20, height: 20 }} />), header: () => null
        }}
        component={AddVehicle} />

      <Tab.Screen name="VehicleInfo" options={{
        tabBarIcon: () => (<Image source={require("../assets/icon/info3.png")} style={{ width: 20, height: 20 }} />), header: () => null
      }}
        component={VehicleInfo} />

      <Tab.Screen name="Update" options={{
        tabBarIcon: () => (<Image source={require("../assets/icon/update.png")} style={{ width: 20, height: 20 }} />), header: () => null
      }}
        component={UpdateCar} />

    </Tab.Navigator>
  )
}
