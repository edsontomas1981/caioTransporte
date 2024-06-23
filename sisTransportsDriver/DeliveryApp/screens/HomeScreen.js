import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Linking } from 'react-native';
import Icon from 'react-native-vector-icons/FontAwesome';

export default function HomeScreen({ navigation, route }) {
  const [deliveries, setDeliveries] = useState([]);

  useEffect(() => {
    if (route.params && route.params.deliveries) {
      setDeliveries(route.params.deliveries);
    }
  }, [route.params]);

  const openMap = (latitude, longitude) => {
    const url = `https://www.google.com/maps/dir/?api=1&destination=${latitude},${longitude}`;
    Linking.openURL(url).catch(err => console.error('Error opening map:', err));
  };

  return (
    <ScrollView style={styles.container}>
      {deliveries.map((delivery) => (
        <View key={delivery.idDtc} style={styles.card}>
          <Text>{delivery.razao_social}</Text>
          <Text>{delivery.endereco}, nº {delivery.numero},</Text>
          <Text>{delivery.complemento}</Text>
          <Text>{delivery.bairro}</Text>
          <Text>{delivery.cidade} - {delivery.uf}</Text>
          <View style={styles.viewMiniBtns}>
            <TouchableOpacity style={styles.miniBtns} onPress={() => navigation.navigate('Coleta de assinatura', { delivery })}>
              <Icon name="edit" size={30} color="#302b2d" />
            </TouchableOpacity>
            <TouchableOpacity style={styles.miniBtnsMeio} onPress={() => navigation.navigate('Comprovantes de entrega', { delivery })} >
              <Icon name="camera" size={20} color="#302b2d" />
            </TouchableOpacity>
            <TouchableOpacity style={styles.miniBtnsMeio} onPress={() => openMap(delivery.latitude, delivery.longitude)}>
              <Icon name="map" size={20} color="#302b2d" />
            </TouchableOpacity>
            <TouchableOpacity style={styles.miniBtnsMeio} onPress={() => {/* Enviar localização para API */}} >
              <Icon name="map-marker" size={20} color="#302b2d" />
            </TouchableOpacity>
            <TouchableOpacity style={styles.miniBtnsMeio} onPress={() => navigation.navigate('Barcode', { delivery })}>
              <Icon name="barcode" size={20} color="#302b2d" />
            </TouchableOpacity>
          </View>
        </View>
      ))}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#15546c',
  },
  card: {
    backgroundColor: '#addd4f',
    padding: 16,
    marginBottom: 16,
    borderRadius: 8,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  miniBtns: {
    padding: 10,
    backgroundColor: '#d9dadc',
    borderRadius: 10,
    alignItems: 'center',
    justifyContent: 'center',
    flex: 1, // Ocupa espaço proporcional na row

  },
  miniBtnsMeio: {
    padding: 10,
    backgroundColor: '#d9dadc',
    borderRadius: 10,
    marginLeft: 10,
    alignItems: 'center',
    justifyContent: 'center',
    flex: 1, // Ocupa espaço proporcional na row
  },
  viewMiniBtns: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    flex: 1, // Ocupa espaço proporcional na row
    backgroundColor: '#6a636d',
    padding: 10,
    borderRadius: 15,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
});
