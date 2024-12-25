import React from "react";

function UserComplaint({ title, complaint, type }) {
  return (
    <div className="complaint">
      <div className="img-and-title-cont">
        <img className="user-image" src="../public/user.png" />
        <h4 className="complaint-title">{title}</h4>
        <div className="complaint-type">{type}</div>
      </div>
      <p className="complaint-describe">{complaint}</p>
    </div>
  );
}

export default UserComplaint;

