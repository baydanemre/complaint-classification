import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import axios from "axios";

// Şikayet ekleme (POST)
export const PostComplaint = createAsyncThunk(
  "/add_complaint",
  async ({ title, complaint }) => {
    const response = await axios.post("http://localhost:8000/add_complaint/", {
      title: title,
      complaint: complaint,
    });
    return response.data;
  }
);

// Son 5 şikayeti alma (GET)
export const FetchRecentComplaints = createAsyncThunk(
  "/recent_complaints",
  async () => {
    const response = await axios.get("http://localhost:8000/recent_complaints/");
    return response.data.complaints;
  }
);

const initialState = {
  title: "",
  complaint: "",
  type: "",
  complaints: [],
};

export const complaint_operations = createSlice({
  name: "complaint",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(PostComplaint.fulfilled, (state, action) => {
      state.title = action.payload.title;
      state.complaint = action.payload.complaint;
      state.type = action.payload.type;
    });
    builder.addCase(FetchRecentComplaints.fulfilled, (state, action) => {
      state.complaints = action.payload;
    });
  },
});

export default complaint_operations.reducer;

