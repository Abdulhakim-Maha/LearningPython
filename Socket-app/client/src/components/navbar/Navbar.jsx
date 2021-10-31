import React, { useEffect, useState } from "react";
import "./Navbar.css";
import Notification from "../../img/notification.svg";
import Message from "../../img/message.svg";
import Settings from "../../img/settings.svg";

const Navbar = ({ socket }) => {
  const [notification, setNotification] = useState([]);
  const [open, setOpen] = useState(false);
  useEffect(() => {
    socket.on("getNotification", (data) => {
      setNotification((prev) => [...prev, data]);
    });
  }, [socket]);
  console.log(notification);

  const displayNotification = (senderName, text) => {
    let action;
    // if (type === 1) {
    //   action = "like";
    // } else if (type === 2) {
    //   action = "comment";
    // } else if (type === 3) {
    //   action = "shared";
    // }
    return (
      <span className="notification">{`${senderName} ${text} your post`}</span>
    );
  };
  const handleRead = () => {
    setNotification([]);
    setOpen(false);
  };
  return (
    <div className="navbar">
      <span className="logo">Mine App</span>
      <div className="icons">
        <div className="icon" onClick={() => setOpen(!open)}>
          <img src={Notification} className="iconImg" alt="" />
          {notification.length > 0 && (
            <div className="counter">{notification.length}</div>
          )}
        </div>
        <div className="icon" onClick={() => setOpen(!open)}>
          <img src={Message} className="iconImg" alt="" />
        </div>
        <div className="icon" onClick={() => setOpen(!open)}>
          <img src={Settings} className="iconImg" alt="" />
        </div>
      </div>
      {open && (
        <div className="notifications">
          {notification.map((n) => displayNotification(n))}
          <button className="nButton" onClick={handleRead}>
            Mark as read
          </button>
        </div>
      )}
    </div>
  );
};

export default Navbar;
