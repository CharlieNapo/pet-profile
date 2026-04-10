import Link from "next/link";
import { notFound } from "next/navigation";
import { getPetById } from "@/lib/api";
import DocumentList from "@/components/DocumentList";
import styles from "./page.module.css";

type Props = {
  params: Promise<{ id: string }>;
};

export default async function PetDetailPage({ params }: Props) {
  const { id } = await params;
  const pet = await getPetById(id);

  if (!pet) {
    notFound();
  }

  return (
    <div>
      <Link href="/" className={styles.back}>
        &larr; Back to list
      </Link>
      <h1 className={styles.name}>{pet.name}</h1>
      <dl className={styles.details}>
        <dt>Species</dt>
        <dd>{pet.species}</dd>
        <dt>Gender</dt>
        <dd>{pet.gender}</dd>
        <dt>Date of Birth</dt>
        <dd>{pet.date_of_birth}</dd>
        <dt>Created</dt>
        <dd>{pet.created_at}</dd>
        <dt>Updated</dt>
        <dd>{pet.updated_at}</dd>
      </dl>
      <h2>Documents</h2>
      <DocumentList documents={pet.documents} />
    </div>
  );
}
