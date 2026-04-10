import Link from "next/link";

export default function NotFound() {
  return (
    <div>
      <h2>Pet not found</h2>
      <p>The pet you are looking for does not exist.</p>
      <Link href="/">Back to pet list</Link>
    </div>
  );
}
