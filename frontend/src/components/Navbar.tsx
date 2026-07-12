import { Link } from "react-router-dom";
import logo from "../assets/cat-logo.png";
import { useAuth } from "../context/AuthContext";

export default function Navbar() {
    const { token, logout } = useAuth();

    return (
        <nav className="navbar">
            <Link to="/" className="logo">
                <img src={logo} alt="StudyFlow Logo" />
                <h2>StudyFlow</h2>
            </Link>

            <div className="nav-links">
                <Link to="/">Home</Link>

                <Link to="/courses">Courses</Link>

                {!token ? (
                    <>
                        <Link to="/login">Sign In</Link>
                        <Link to="/register">Register</Link>
                    </>
                ) : (
                    <>
                        <Link to="/my-courses">My Courses</Link>

                        <a
                            href="#"
                            onClick={(e) => {
                                e.preventDefault();
                                logout();
                            }}
                        >
                            Logout
                        </a>
                    </>
                )}
            </div>
        </nav>
    );
}