import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { PostComplaint, FetchRecentComplaints } from "../redux/slices/complaint_operations";
import { setTitle, setComplaint } from "../redux/slices/user_complaint_input";

function CreateComplaint() {
  const dispatch = useDispatch();
  const { input_title: title, input_complaint: complaint } = useSelector(
    (store) => store.user_inputs
  );

  const handleSubmit = async () => {
    if (title.trim() && complaint.trim()) {
      await dispatch(PostComplaint({ title, complaint }));
      dispatch(FetchRecentComplaints()); // Tabloyu güncelle
      alert("Complaint submitted successfully!");
      dispatch(setTitle(""));
      dispatch(setComplaint(""));
    } else {
      alert("Please fill in both the title and complaint.");
    }
  };

  return (
    <div className="create-complaint">
      <h4>Create Complaint</h4>
      <input
        className="title-field"
        type="text"
        placeholder="Enter your title"
        onChange={(e) => dispatch(setTitle(e.target.value))}
        value={title}
      />
      <textarea
        className="complaint-field"
        placeholder="Enter your complaint"
        onChange={(e) => dispatch(setComplaint(e.target.value))}
        value={complaint}
      ></textarea>
      <button className="check-complaint-button" onClick={handleSubmit}>
        Check
      </button>
    </div>
  );
}

export default CreateComplaint;


