import { Link } from "react-router-dom";

export default function HomePage() {
    return (
        <main className="hero">
            <h1>StudyFlow</h1>

            <p>
                Learn. Build. Grow.
            </p>

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