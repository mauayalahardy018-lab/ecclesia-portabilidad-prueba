import { Router } from "express";
import { z } from "zod";
import { createTask } from "./service.js";

const router = Router();
const input = z.object({ title: z.string().trim().min(3).max(120) });

router.post("/tasks", async (req, res, next) => {
  try {
    res.status(201).json(await createTask(input.parse(req.body)));
  } catch (error) {
    next(error);
  }
});

export default router;
