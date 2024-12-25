// src/app/store.js
import { configureStore } from '@reduxjs/toolkit';
import complaintReducer from '../redux/slices/complaint_operations';
import userInputReducer from '../redux/slices/user_complaint_input';
import createComplaintRowReducer from '../redux/slices/create_complaint_row';

export const store = configureStore({
  reducer: {
    user_inputs: userInputReducer,
    complaint: complaintReducer,
    complaint_rows: createComplaintRowReducer
  },
});
