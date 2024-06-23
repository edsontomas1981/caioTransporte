import React, { useState } from 'react';
import { Alert, ActivityIndicator } from 'react-native';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ImageBackground } from 'react-native';
import Icon from 'react-native-vector-icons/FontAwesome';
import { fetchAPI } from '../tasks/conectaApi';

export default function LoginScreen({ navigation }) {
  const [cpf, setCpf] = useState('');
  const [loading, setLoading] = useState(false);

  const handleLogin = async () => {
    if (!cpf) {
      Alert.alert('CPF não informado', 'Por favor, informe o CPF.');
      return;
    }

    setLoading(true);

    const url = `http://sistransportslog.tech/appMotoristas/get_dados/`;
    const dados = { cpf: cpf };
    try {
      const data = await fetchAPI(url, 'POST', dados);

      if (data && data.dados) {
        navigation.navigate('HomeStack', { screen: 'Home', params: { deliveries: data.dados } });
      } else {
        Alert.alert('Erro de autenticação', 'CPF ou senha inválidos.');
      }
    } catch (error) {
      Alert.alert('Erro', 'Ocorreu um erro ao tentar fazer login. Por favor, tente novamente.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <ImageBackground source={require('../assets/images/background.png')} style={styles.background}>
      <View style={styles.container}>
        <TextInput
          style={styles.input}
          placeholder="CPF"
          placeholderTextColor="#999"
          keyboardType="numeric"
          value={cpf}
          onChangeText={setCpf}
        />

        <TouchableOpacity style={styles.btnEntrar} onPress={handleLogin} disabled={loading}>
          <Icon name="sign-in" size={35} color="#999" />
          <Text style={styles.btnEntrarText}> ENTRAR</Text>
        </TouchableOpacity>
        {loading && <ActivityIndicator
                      size={60}          // Tamanho grande
                      color="#a46e5c"    // Cor laranja
                      style={{ margin: 10 }} // Margem de 10 pixels
                      animating={true}
                  />}
      </View>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 16,
  },
  background: {
    flex: 1,
    width: '100%',
    height: '100%',
    justifyContent: 'center',
    backgroundColor: '#cac7bf',
  },
  btnEntrar: {
    flexDirection: 'row',
    color: 'white',
    fontSize: 24,
    alignItems: 'center',
    justifyContent: 'center',
  },
  btnEntrarText: {
    flexDirection: 'row',
    color: "#999",
    fontSize: 24,
  },
  input: {
    height: 40,
    borderColor: '#ccc',
    borderWidth: 1,
    marginBottom: 16,
    paddingHorizontal: 8,
    borderRadius: 15,
    color: 'white',
  },
});
