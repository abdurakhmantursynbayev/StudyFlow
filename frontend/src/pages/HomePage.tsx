import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { getMe } from "../api/user";
import type { User } from "../types/user";

export default function HomePage() {
    const [user, setUser] = useState<User | null>(null);

    useEffect(() => {
        async function loadUser() {
            try {
                const data = await getMe();
                setUser(data);
            } catch {
                setUser(null);
            }
        }

        loadUser();
    }, []);

    return (
        <main className="hero">
            <h1>StudyFlow</h1>

            {user ? (
                <p>
                    Welcome, <strong>{user.full_name}</strong> ({user.role})
                </p>
            ) : (
                <p>Learn. Build. Grow.</p>
            )}

            <span>
                Modern learning platform powered by
                <strong> FastAPI</strong>,
                <strong> React</strong> and
                <strong> PostgreSQL</strong>.
            </span>

            <Link to="/courses" className="hero-button">
                Browse Courses
            </Link>
        </main>
    );
}