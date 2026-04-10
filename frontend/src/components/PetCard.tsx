import Link from "next/link";
import type { Pet } from "@/lib/api";
import styles from "./PetCard.module.css";

interface Props {
  pet: Pet;
}

export default function PetCard({ pet }: Props) {
  return (
    <div className={styles.card}>
      <Link href={`/pets/${pet.id}`} className={styles.name}>
        {pet.name}
      </Link>
      <div className={styles.details}>
        <span className={styles.badge}>{pet.species}</span>
        <span className={styles.badge}>{pet.gender}</span>
        <span>Born {pet.date_of_birth}</span>
      </div>
      <div className={styles.docs}>
        {pet.documents.length}{" "}
        {pet.documents.length === 1 ? "document" : "documents"}
      </div>
    </div>
  );
}
