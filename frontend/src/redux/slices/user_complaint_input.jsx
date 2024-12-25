// src/features/counter/counterSlice.js
import {  createSlice } from '@reduxjs/toolkit';

const initialState = {
  input_title: "",
  input_complaint: ""
}

export const user_complaint_input = createSlice({
  name: 'user_inputs',
  initialState,
  reducers: {
    setTitle: (state,action) => {
        state.input_title = action.payload
    },
    setComplaint: (state,action) => {
        state.input_complaint = action.payload
    },

  },
});

export const {setTitle,setComplaint} = user_complaint_input.actions;

export default user_complaint_input.reducer;