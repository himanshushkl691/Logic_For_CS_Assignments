Require Import Classical_Prop.
Lemma demorgan : forall P Q : Prop, ~(~P /\ ~Q) -> (P \/ Q).
Proof.
  intros P Q.
  intro H1.
  apply NNPP.
  unfold not.
  intro H2.
  case H1.
  split.
  unfold not.
  intro H3.
  apply H2.
  left.
  exact H3.
  unfold not.
  intro H3.
  apply H2.
  right.
  exact H3.
Qed.
Lemma implies_left : forall P Q : Prop, (~P -> Q) -> (P \/ Q).
Proof.
  intros P Q.
  intro H1.
  apply demorgan.
  unfold not.
  intro H2.
  destruct H2 as [H2 H3].
  apply H3.
  apply H1.
  unfold not.
  exact H2.
Qed.
Lemma implies_right : forall P Q : Prop,(~P \/ Q) -> (P -> Q).
Proof.
  intros P Q.
  intro H1.
  intro H2.
  case H1.
  intro H3.
  unfold not in H3.
  apply H3 in H2.
  elim H2.
  intro H3.
  exact H3.
Qed.
Section Prop_Logic_Assg2A.
(* {} |- (p->q)|(q->r) *)
Variable P Q R : Prop.
Lemma ASSG2A_7 : (P -> Q) \/ (Q -> R).
Proof.
  apply implies_left.
  intro H1.
  apply implies_right.
  left.
  unfold not.
  unfold not in H1.
  intro H2.
  apply H1.
  intro H3.
  exact H2.
Qed.