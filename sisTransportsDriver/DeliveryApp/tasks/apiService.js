import { Alert } from 'react-native';

export const fetchData = async (url, setData) => {
  try {
    const response = await fetch(url);

    // Handle network errors or unreachable servers
    if (!response.ok) {
      throw new Error(`Network error! Status: ${response.status}`);
    }

    // Parse and set data, even if it's an empty array/object (to indicate "no results")
    const data = await response.json();
    setData(data);

  } catch (error) {
    // Centralized Error Handling and User Feedback
    console.error("Error fetching data:", error.message);

    // Tailor alerts to different error types if needed
    if (error.message.startsWith('Network error')) {
      Alert.alert("No Connection", "Please check your internet and try again.");
    } else {
      Alert.alert("Error", "Something went wrong while fetching data.");
    }
  }
};

