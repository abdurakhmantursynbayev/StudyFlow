import { useNavigate } from "react-router-dom";
import { useState } from "react";

import { login as loginRequest } from "../api/auth";
import { useAuth } from "../context/AuthContext";

export default function LoginPage() {
    const navigate = useNavigate();

    const { login } = useAuth();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    async function handleSubmit(e: React.FormEvent) {
        e.preventDefault();

        try {
            const data = await loginRequest(username, password);

            login(data.access_token);

            navigate("/");
        } catch {
            alert("Invalid username or password");
        }
    }

    return (
        <main className="auth-page">
            <div className="auth-card">
                <h1>Sign In</h1>

                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        placeholder="Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />

                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />

                    <button type="submit">
                        Sign In
                    </button>
                </form>
            </div>
        </main>
    );
}