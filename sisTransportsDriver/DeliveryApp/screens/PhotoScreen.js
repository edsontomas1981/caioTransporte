import React, { useState, useEffect } from 'react';
import { View, Text, Button, Image, StyleSheet, Alert, TouchableOpacity } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import { fetchAPI } from '../tasks/conectApiFoto';
import { manipulateAsync } from 'expo-image-manipulator';
import Icon from 'react-native-vector-icons/FontAwesome';

export default function PhotoScreen({ route }) {
  const { delivery } = route.params;
  const [image, setImage] = useState(null);


  useEffect(() => {
    (async () => {
      const { status } = await ImagePicker.requestCameraPermissionsAsync();
      if (status !== 'granted') {
        Alert.alert('Permissão necessária', 'Precisamos da permissão da câmera para continuar');
      }
    })();
  }, []);

  const pickImage = async () => {
  let result = await ImagePicker.launchCameraAsync({
    mediaTypes: ImagePicker.MediaTypeOptions.Images,
    allowsEditing: false,
    quality: 1,
  });

  console.log('Resultado da captura:', result);

  if (!result.cancelled) {
    if (result.assets && result.assets.length > 0) {
      try {
        const imageUri = result.assets[0].uri;
        const manipResult = await manipulateAsync(
          imageUri,
          [{ resize: { width: 800 } }],
          { compress: 0.8, format: 'jpeg' }
        );

        setImage(manipResult.uri);
        console.log('Imagem definida:', manipResult.uri);
      } catch (error) {
        console.error('Erro ao manipular imagem:', error);
      }
    } else {
      console.log('Nenhuma imagem disponível');
    }
  } else {
    console.log('Captura de imagem cancelada');
  }
};


  const handleSendPhoto = async () => {

    if (!image) {
      console.log('Image is null or undefined');
      return;
    }

    try {
      const formData = new FormData();
      console.log(delivery)

      formData.append('idNf',delivery.idDtc);
      formData.append('ocorrencia_fk', 4);
      // formData.append('nota_fiscal_fk', delivery.nota_fiscal_fk);
      // formData.append('observacao', delivery.observacao);
      formData.append('data', new Date().toISOString());

      const fileType = image.substring(image.lastIndexOf('.') + 1);
      const fileName = image.split('/').pop();
      const fileData = {
        uri: image,
        name: fileName,
        type: `image/${fileType}`
      };
      formData.append('imagem', fileData);
      formData.idDtc = delivery.idDtc

      const response = await fetchAPI('http://sistransportslog.tech/appMotoristas/add_ocorrencia/', 'POST', formData, true);
      if (response && response.status === 200) {
        alert('Foto enviada com sucesso!');
      } else {
        alert('Erro ao enviar foto.');
      }
    } catch (error) {
      console.error('Error in handleSendPhoto:', error);
      alert('Erro ao enviar foto.');
    }
  };

  return (
    <View style={styles.container}>
      {image && <Image source={{ uri: image }} style={styles.image} />}
        <View style={styles.buttonContainer}>
          <TouchableOpacity style={styles.btnEntrar} onPress={pickImage}>
            <Icon name="camera" size={35} color="#999" />
            <Text style={styles.btnEntrarText}>Capturar</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.btnEntrar} onPress={handleSendPhoto} >
            <Icon name="paper-plane" size={35} color="#999" />
            <Text style={styles.btnEntrarText}>Enviar</Text>
          </TouchableOpacity>
        </View>
    </View>
  );
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      padding: 16,
    },
    image: {
      width: 350,
      height: 200,
      marginTop: 16,
    },
    buttonContainer: {
      flexDirection: 'row',
      justifyContent: 'space-around', // Distribui os botões uniformemente
      marginTop: 16,
      width: '100%', // Ocupa toda a largura do container pai
    },
    btnEntrar: {
      flex: 1, // Faz os botões ocuparem espaço igual na linha
      flexDirection: 'row',
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#6a636d',
      borderRadius: 10,
      paddingHorizontal: '5%', // Padding horizontal relativo à largura
      paddingVertical: '2.5%', // Padding vertical relativo à altura
    },
    btnEntrarText:{
      flexDirection:'row',

      justifyContent: 'center',
      alignItems: 'center',
      color:'white',
      fontSize:14,
      alignItems:'center',
      padding:5,
      borderRadius:10,
      justifyContent:'center',
    },
});
