import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { FetchRecentComplaints } from "../redux/slices/complaint_operations";
import UserComplaint from "./UserComplaint";

const ComplaintBox = () => {
  const dispatch = useDispatch();
  const complaints = useSelector((store) => store.complaint.complaints);

  useEffect(() => {
    dispatch(FetchRecentComplaints()); // İlk yüklemede tabloyu doldur
  }, []);

  return (
    <div className="complaint-box">
      <h4>Complaint Box</h4>
      <div className="complaints-container">
        {complaints.map((complaint, index) => (
          <UserComplaint
            key={index}
            title={complaint.title}
            complaint={complaint.complaint}
            type={complaint.type}
          />
        ))}
      </div>
    </div>
  );
};

export default ComplaintBox;


