// src/features/counter/counterSlice.js
import {  createSlice } from '@reduxjs/toolkit';

const initialState = {
  complaint_row: [],
}

export const create_complaint_row = createSlice({
  name: 'complaint_rows',
  initialState,
  reducers: {
    addNewComplaint: (state, action) => {
      const id = state.complaint_row.length + 1;
      state.complaint_row.push({
        id: id,
        title: action.payload.title,
        complaint: action.payload.complaint,
        type: action.payload.type, // Redux store'daki 'type' bilgisi
      });
    }
    
  },
});

export const {addNewComplaint} = create_complaint_row.actions;

export default create_complaint_row.reducer;