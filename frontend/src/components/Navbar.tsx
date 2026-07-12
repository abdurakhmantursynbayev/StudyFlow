import { Link } from "react-router-dom";
import catLogo from "../assets/cat-logo.png";

export default function Navbar() {
    return (
        <nav className="navbar">
            <div className="logo">
                <img src={catLogo} alt="StudyFlow Logo" />
                <h2>StudyFlow</h2>
            </div>

            <div className="nav-links">
                <Link to="/">Home</Link>
                <Link to="/courses">Courses</Link>
                <Link to="/login">Sign In</Link>
                <Link to="/register">Register</Link>
            </div>
        </nav>
    );
}